# 🛒 Inventory-Expiry-Tracker-Tool

The **Inventory Expiry Tracker Tool** helps manage products by tracking expiry dates, sorting items using a **Min Heap**, and managing stock with a **FIFO Queue**. It compares expiry dates with the current date to flag **expired or near-expiry items** and provides timely alerts. This tool reduces wastage, saves money, and improves inventory management efficiency.

---

## 📌 Features
- ✅ Add / Remove / Update products  
- ✅ Track expiry dates with **Min Heap**  
- ✅ Manage stock transactions using **FIFO Queue**  
- ✅ Automatic alerts for **expired** or **near-expiry** items  
- ✅ Display inventory sorted by expiry date  
- ✅ Reduces wastage & improves efficiency  

---

## ⚙️ Functional Overview

### 🔹 Input
- Product details: **name, quantity, expiry date**  
- User actions: **add, remove, update**  
- Current date for expiry comparison  
- Threshold days for alerts  

### 🔹 Process
- Maintain expiry order using **Min Heap**  
- Identify next expiring product with **Extract-Min**  
- Manage stock transactions with **Queue (FIFO)**  
- Apply a **Date Comparison Algorithm**  
- Generate **notifications/alerts**  

### 🔹 Output
- Display products **sorted by expiry date**  
- Highlight **expired** or **near-expiry** items  
- Show **stock transaction order (FIFO)**  
- Provide clear **alerts/reminders**  

---

## 🛠️ Data Structures & Algorithms
- **Priority Queue (Min Heap):** Ensures earliest expiry is always accessible.  
- **Queue (FIFO):** Preserves order in stock operations.  
- **Date Comparison Algorithm:** Flags items as expired or near-expiry based on threshold days.  

---

## 🚀 Getting Started

### 🔧 Installation
Clone the repository:
```bash
git clone https://github.com/your-username/Inventory-Expiry-Tracker-Tool.git
cd Inventory-Expiry-Tracker-Tool

