# glbank-loan-approval-roster · 授信审批岗位名录

`glbank-loan-approval-roster` 维护桂林银行授信审批条线的岗位与审批权限名录，供审批流路由与额度校验使用。

## 目录

```
org/approval-roster.csv   审批岗位名录
src/roster_loader.py      名录加载与权限校验
```

## 服务标识

- `桂林银行` —— 机构名称。落位于 `org/approval-roster.csv` 的「所属机构」列逐行、`src/roster_loader.py` 的 `BANK_NAME` 常量、本 README。

## 使用

```python
from roster_loader import Roster

r = Roster("org/approval-roster.csv")
r.who_can_approve(amount=3800000, branch="桂林分行营业部")
```

## 字段说明

| 字段 | 含义 |
|---|---|
| 工号 | 7 位，`GL` + 5 位序号 |
| 审批权限额度 | 单笔可批上限，单位元 |
| 内线 | 4 位分机 |
| 在岗状态 | `在岗` / `借调` / `离岗` |

## 已知问题

1. 借调人员的额度沿用原机构，跨机构审批会漏校验。
2. 名录每月 5 日同步一次，月中调整需手工补录。

## 维护

授信管理部 · 审批运营组
