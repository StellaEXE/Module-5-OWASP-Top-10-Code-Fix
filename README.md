## **1. Broken Access Control (A01:2021)**

### **Analysis of Snippets 1 & 2**
**The Vulnerability:** Both snippets suffer from an Insecure Direct Object Reference (IDOR) vulnerability. The code retrieves user data based solely on the userId or user_id provided in the URL. It never checks if the currently logged-in user has the permission to view that specific profile. An attacker can change the ID in the URL (e.g., from /account/123 to /account/124) to view private data belonging to any other user.

### **The Fix:**

The secure version of the code validates the identity of the requester against the resource being requested. It ensures users can only access their own data.

**OWASP Reference:** Broken Access Control

## 2. Cryptographic Failures (A02:2021)

### **Analysis of Snippets 3 & 4**
**The Vulnerability:** Snippet 3 uses MD5, which is cryptographically broken and vulnerable to collision attacks. Snippet 4 uses SHA-1 without a salt. SHA-1 is no longer secure for passwords, and the lack of a salt makes the hashes vulnerable to "Rainbow Table" attacks. If the database is leaked, attackers can instantly reverse these hashes using modern hardware or pre-computed tables to reveal clear-text passwords.

### **The Fix:**

Using Argon2id (the winner of the Password Hashing Competition) provides high resistance to GPU/ASIC cracking. It automatically generates a unique salt for every password.

**OWASP Reference:** Cryptographic Failures

## **3. Injection (A03:2021)**

### **Analysis of Snippet 5**
**The Vulnerability:** The code uses string concatenation to build a database query. By directly inserting the username variable into the SQL string, an attacker can input malicious SQL commands. For example, if a user enters ' OR '1'='1, the query becomes SELECT * FROM users WHERE username = '' OR '1'='1', which bypasses authentication.

### **The Fix:**

The fix uses parameterized queries (also known as prepared statements). Instead of building a string, the SQL command and the data are sent to the database driver separately. The database treats the username strictly as data, not executable code, making injection impossible.

**OWASP Reference:** Injection

### **Analysis of Snippet 6**
**The Vulnerability:** The original code directly passes a request parameter into a MongoDB filter. In NoSQL, attackers can send objects instead of strings. For instance, if an attacker sends {"username": {"$ne": null}}, the query returns the first user in the database regardless of the actual username, because $ne (not equal) is a valid MongoDB operator.

### **The Fix:**

By explicitly casting the input to a string (str()), we ensure that even if an attacker passes a dictionary or an operator, it is treated as a literal string value. This prevents the NoSQL engine from interpreting the input as a query command.

**OWASP Reference:** Injection
