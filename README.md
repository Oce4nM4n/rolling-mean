# Forecasted Cost Generator

This Python script reads a dataset of customer resource costs, predicts costs for additional future months, and appends these forecasts to the dataset.

---

## 📄 **How it works**

* Loads data from `data.csv`.
* Iterates through each unique `customerid` and their associated `resourceid`.
* For each combination:

  * Identifies the latest 3 months of data.
  * Calculates the average `cost` across those 3 months.
  * Creates forecasted entries for `predictedmonths` future months, each with:

    * The same `customerid`
    * The same `resourceid`
    * The average of the latest 3 months as the forecasted cost
    * The next chronological month number (latest month + 1, +2, etc.)
  * Appends these forecasted entries to the dataset.
* Saves the full dataset (original + forecasted data) to `forecasted_data.csv`.

---

## 📥 **Input**

* **`data.csv`**

  * Expected columns:

    * `customerid` (string)
    * `resourceid` (string)
    * `cost` (numeric)
    * `month` (integer, representing month as double-digit number or sequential month count)

---

## 📤 **Output**

* **`forecasted_data.csv`**

  * Contains the original data and the forecasted rows.

---

## 📝 **Example flow**

For each customer + resource:

```
Customer ID: A
Resource ID: X
Latest months: [6, 5, 4]
Forecasted data for customer A, resource X:
  customerid resourceid  cost  month
0          A          X  150.0      7
```


## 🚀 **How to run**

1️⃣ Make sure you have **pandas** installed:

```bash
pip install pandas
```

2️⃣ Place `data.csv` in the same directory as the script.

3️⃣ Run the script:

```bash
python main.py
```

4️⃣ The output will be saved as `forecasted_data.csv`.

