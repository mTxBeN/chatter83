# Chatter83 🧠💬  
*A lightweight chatbot for the TI-83 Premium CE Python Edition*

## 📌 What is Chatter83?  
Chatter83 is a **tiny but efficient chatbot** built entirely in **Python** for the **TI-83 Premium CE** calculator. It allows users to ask simple questions and receive relevant responses based on a **predefined knowledge base**. The main challenge was **fitting everything within the calculator's extreme memory constraints**, while keeping it as intelligent as possible.

Unlike advanced AI models, **Chatter83 does not "learn"** dynamically—it **matches input text to the closest stored question** and retrieves the best possible answer.

---

## 🚧 The Journey: Problems & Challenges We Faced  

### 1️⃣ **Fitting everything in a tiny space**  
The **TI-83 Premium CE** only has **154KB of RAM**, and **Python on the calculator is even more limited**. Standard chatbot implementations wouldn't work, so we had to **compress data to the extreme**.

### 2️⃣ **Many failed attempts**  
Before arriving at the current solution, we tried multiple approaches:  

❌ **Markov Chains** – Too random, not useful for Q&A.  
❌ **Weights & Neural Networks** – Too much RAM usage.  
❌ **Exact String Matching** – Not flexible enough.  
✅ **Compressed Dictionary & Scoring System** – This worked!  

### 3️⃣ **Keeping the chatbot intelligent despite memory limits**  
To make the chatbot as accurate as possible while **using minimal RAM**, we developed a **custom matching algorithm** that:  
✔️ Assigns **scores** to words based on importance.  
✔️ **Compresses** words into numeric IDs instead of storing full sentences.  
✔️ Uses **multiple small `.py` files** instead of a single large one to bypass memory errors.  

---

## 🛠️ How Chatter83 Works  

### 🔍 **Finding the Closest Match Using Scores**  
Instead of storing full sentences, **Chatter83 breaks everything into word IDs**. When a user asks a question:  
1. It **converts the input into word IDs**.  
2. It **compares it to stored questions** and selects the **closest match**.  
3. It **retrieves the associated answer**, reconstructing it from compressed IDs.  

### 🏗️ **Memory-Saving Techniques**  
- **Only decodes the answer AFTER finding the match** (saves processing power by only decoding the good answer).  
- **Uses word IDs instead of full sentences** (saves bytes).  
- **Splits the database into multiple `.py` files** (avoids `MemoryError`).  
- **Smallest file size** by removing unnecessary comments & long variable names.  

### 🧐 See for Yourself – Understanding the Code  

If you're curious about how **Chatter83** works under the hood, a **version of `chatter83.py` with more detail** is available. This version:  
- Uses **full variable names** instead of shortened ones to save space.
- Includes **detailed comments** explaining the logic.  
- Can print **debugging information** to show how it finds the best response.  

You can find it in the repository as **`chatter83_verbose.py`**. This version is meant for **learning and experimentation**, while **`chatter83.py`** is the fully optimized version designed to run on the **TI-83 Premium CE** with minimal memory usage.  

To toggle **debugging mode**, change `DEBUG =` to your preferred state. It is enabled by default. This will display **score calculations, word matching, and other internals**.  

---

## 📥 How to Install & Use Chatter83  

### 🔹 **Installing on Your Calculator**  
1. **Download the files** from this repository.  
2. **Transfer them** to your **TI-83 Premium CE** using **TI-Connect CE**.  
3. **Ensure all required files are copied**, including:  
   - `w.py` → Word list  
   - `sdata.py` → Score dictionary  
   - `kp1.py`, `kp2.py`, etc. → Knowledge base chunks  
   - `chatter83.py` → The main chatbot script  

### 🔹 **Running the Chatbot**  
1. Open the Python app on your **TI-83 Premium CE**.  
2. Navigate to **`chatter83.py`** and run it.  
3. Type in a question and get a response!  
4. Type **`exit`** to quit the chatbot.  
5. Type **`verbose`** to enable debug mode. In this mode, you will see how the bot decides what is the best answer.

---

## 🛠️ Customizing Chatter83: Train Your Own AI  

The current chatbot has a **limited knowledge** because of the low memory space. Want to make **Chatter83** answer your own questions? **Here's how:**  

### **1️⃣ Download and Edit the Knowledge Base**  
- Open `data.txt` and write your **questions & answers** in a simple format.  
- Note that it is important to **not add many Q&A pairs as they will take space**. We recommend **maximum 20**. You will see if your calculator gives a `MemoryError`, you need to reduce.

### **2️⃣ Run the Converter Script**  
- The provided script (`train.py`) **automatically converts `data.txt` into compressed `.py` files**:
  - Generates **word scores** (`sdata.py`).  
  - Compresses **word lists** (`w.py`).  
  - Splits **knowledge into multiple files** (`kp1.py`, `kp2.py`, etc.).  

### **3️⃣ Transfer the New Files**  
- Copy the newly generated `.py` files to your calculator.
- Done! **Your chatbot is now customized.**  🎉  

---

## 🚀 Future Improvements  

✅ **Improve response accuracy** – Enhance matching algorithm.  
✅ **Optimize memory usage** – Free up space to allow more Q&A pairs while maintaining performance.  
✅ **Rewrite the chatbot in C** – **Exploring a C-to-assembly rewrite** to remove Python’s memory limits and take full advantage of the calculator’s hardware. This could massively improve performance.  
✅ **Enable dynamic learning** – If feasible, allow the chatbot to store new Q&A pairs dynamically.  

---

## 🤝 Contributing  

Want to help improve **Chatter83**? Contributions are welcome!  

### 🔹 **Ways to Contribute:**  
- Add **new Q&A pairs** to expand the chatbot’s knowledge.  
- Optimize the **Python code** for better memory usage.  
- Help with the **future C implementation**.  

Simply fork the repo, make changes, and submit a **pull request**!  

---

## 📜 License  

**Chatter83** is open-source and released under the **MIT License**. See the **`LICENSE` file** for more information. Feel free to modify, share, and improve it!  

---

## 🛠️ Need Help?  

If you encounter any problems while setting up or using **Chatter83**, feel free to **open an issue** on GitHub. Whether it's a bug, a memory issue, or a feature request, I'll do my best to help! 🚀

---

### 🎉 *Enjoy using Chatter83 on your TI-83 Premium CE!* 🎉  
