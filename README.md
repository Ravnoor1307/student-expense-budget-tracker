# Student Expense Budget Tracker

A desktop expense-tracking project built with Python and Tkinter. The dashboard
shows income and expense summaries, a budget overview, charts, and recent
transactions using the JSON files in `data/`.

## Requirements

- Python 3.8 or newer
- Tkinter (included with most standard Python installations)

No third-party packages are currently required.

## Run the dashboard

From the project directory, run:

```powershell
python dashboard.py
```

The dashboard opens with the current month selected. Select another month from
the month selector to update the monthly totals, charts, and recent
transactions. The sidebar lists the planned application sections; only the
Dashboard view is implemented at this time.

## Data files

The dashboard reads `data/transactions.json` and `data/budgets.json` when it
starts. Both files must contain a top-level array under the indicated key.

Example `data/transactions.json`:

```json
{
  "transactions": [
    {
      "type": "expense",
      "amount": 18.5,
      "date": "2026-11-02",
      "category": "Food",
      "description": "Lunch"
    },
    {
      "type": "income",
      "amount": 250,
      "date": "2026-11-01",
      "category": "Part-time work",
      "description": "Weekly pay"
    }
  ]
}
```

Each transaction requires:

- `type`: `income` or `expense`
- `amount`: a number
- `date`: a date in `YYYY-MM-DD` format

`category` and `description` are optional. If `description` is omitted, the
dashboard uses `title`, then displays `-`.

Example `data/budgets.json`:

```json
{
  "budgets": [
    {
      "amount": 500
    }
  ]
}
```

Each budget entry currently requires an `amount`. The dashboard sums the
entries to calculate the budget overview.

The current data files are empty, so the dashboard initially displays zero
totals and empty chart/table states. Invalid or unreadable JSON data is reported
when the dashboard starts.

## Current limitations

- Login and account creation are not connected to an authentication or account
  storage system.
- Sidebar sections other than Dashboard are placeholders.
- Transactions and budgets must currently be entered in the JSON data files.