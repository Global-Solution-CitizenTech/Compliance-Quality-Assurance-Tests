#!/usr/bin/env python3
"""Testes offline de segurança para SyncEngine, AzureClient e parser_backlog (zero chamadas HTTP)."""

import unittest
from unittest.mock import MagicMock

from azure_client import AzureClient
from parser_backlog import _format_inline_markdown
from sync_engine import SyncEngine


class SafetyGuardsTest(unittest.TestCase):
    def _mock_client(self, items):
        client = MagicMock(spec=AzureClient)
        client.query_wiql.return_value = [it["id"] for it in items]
        client.get_batch.return_value = items
        client.delete_work_item.return_value = True
        client.update_work_item.return_value = True
        return client

    def test_clean_board_preserves_tasks_and_test_cases_and_uses_soft_delete(self):
        items = [
            {"id": 67, "fields": {"System.WorkItemType": "Epic", "System.Title": "Epic QA"}},
            {"id": 220, "fields": {"System.WorkItemType": "Task", "System.Title": "Task Video DevOps"}},
            {"id": 134, "fields": {"System.WorkItemType": "Test Case", "System.Title": "[TC-01]"}},
            {"id": 132, "fields": {"System.WorkItemType": "Test Plan", "System.Title": "api-auth-rbac"}},
        ]
        client = self._mock_client(items)
        engine = SyncEngine(client=client)

        deleted = engine.clean_board()

        self.assertEqual(deleted, 1)
        wiql = client.query_wiql.call_args[0][0]
        self.assertIn("'Epic', 'Feature', 'Product Backlog Item'", wiql)
        client.delete_work_item.assert_called_once_with(67, destroy=False)

    def test_clean_board_dry_run_never_deletes(self):
        items = [{"id": 67, "fields": {"System.WorkItemType": "Epic", "System.Title": "Epic QA"}}]
        client = self._mock_client(items)
        engine = SyncEngine(client=client)

        self.assertEqual(engine.clean_board(dry_run=True), 0)
        client.delete_work_item.assert_not_called()

    def test_apply_governance_skips_tasks_and_test_cases(self):
        items = [
            {"id": 220, "fields": {"System.WorkItemType": "Task", "System.Tags": "DevOps", "System.State": "Doing", "System.Title": "Task DevOps"}},
            {"id": 134, "fields": {"System.WorkItemType": "Test Case", "System.Tags": "Compliance", "System.State": "Ready", "System.Title": "[TC-01]"}},
            {"id": 68, "fields": {"System.WorkItemType": "Feature", "System.Tags": "Compliance", "System.State": "In Progress", "System.Title": "Feat"}},
        ]
        client = self._mock_client(items)
        engine = SyncEngine(client=client)

        updated = engine.apply_governance()

        self.assertEqual(updated, 1)
        client.update_work_item.assert_called_once()
        self.assertEqual(client.update_work_item.call_args[0][0], 68)

    def test_get_batch_chunks_above_200_ids(self):
        client = AzureClient("org", "proj", "fake-pat")
        resp = MagicMock(status_code=200)
        resp.json.return_value = {"value": [{"id": 1}]}
        client.session.post = MagicMock(return_value=resp)

        res = client.get_batch(list(range(1, 451)))

        self.assertEqual(client.session.post.call_count, 3)
        self.assertEqual(len(res), 3)

    def test_inline_markdown_preserves_snake_case_identifiers(self):
        out = _format_inline_markdown("`run_sync.py`, `sync_engine.py`, foo_bar e _enfase_")
        self.assertIn("<code>run_sync.py</code>", out)
        self.assertIn("<code>sync_engine.py</code>", out)
        self.assertIn("foo_bar", out)
        self.assertIn("<em>enfase</em>", out)


if __name__ == "__main__":
    unittest.main()
