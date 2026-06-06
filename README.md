# Natural Language to SQL Analytics Interface (Gemini + LangChain)

An AI-driven data interface that allows business stakeholders to query a relational e-commerce database using plain English. The backend utilizes Google Gemini and LangChain to dynamically evaluate database schemas, construct optimized SQL statements, and retrieve real-time analytics.

## 🚀 Key Frameworks & Tools
- **LLM Engine:** Google Gemini (`gemini-2.5-flash`)
- **Orchestration:** LangChain (`SQLDatabaseChain`)
- **Database Layer:** SQLite & SQLAlchemy
- **Frontend Dashboard:** Streamlit UI

## 📈 Business Features
- **Zero-SQL Analytics:** Empowers non-technical managers to extract insights without writing code.
- **Relational Awareness:** The AI automatically handles primary keys, foreign keys, and table joins between `customers` and `orders`.
- **Dynamic Context Loading:** Inspects schema definitions natively to avoid hallucinated column names.

## 🛠️ Local Installation & Execution

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ai-sql-generator.git](https://github.com/YOUR_USERNAME/ai-sql-generator.git)
   cd ai-sql-generator"# AI-SQL-GENERATOR" 
