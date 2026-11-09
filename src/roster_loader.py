# -*- coding: utf-8 -*-
"""授信审批岗位名录加载。"""
import csv

BANK_NAME = "桂林银行"
ROSTER_ROOT = "org/approval-roster.csv"


class Roster(object):
    def __init__(self, path=ROSTER_ROOT):
        self.path = path
        self.rows = []
        with open(path, newline="", encoding="utf-8-sig") as fh:
            self.rows = [r for r in csv.DictReader(fh)]

    def who_can_approve(self, amount, branch):
        out = []
        for r in self.rows:
            if r["所属机构"] != BANK_NAME + branch:
                continue
            if r["在岗状态"] != "在岗":
                continue
            if int(r["审批权限额度"]) >= amount:
                out.append((r["工号"], r["姓名"], r["内线"]))
        return out

    def escalate(self, amount):
        return [r["工号"] for r in self.rows
                if int(r["审批权限额度"]) >= amount and r["岗位"] == "审批主管"]
