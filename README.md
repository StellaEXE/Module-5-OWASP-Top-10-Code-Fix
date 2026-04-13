## **1 & 2. Broken Access Control (A01:2021)**

### **Analysis of Snippets 1 & 2**
**The Vulnerability:** Both snippets suffer from an Insecure Direct Object Reference (IDOR) vulnerability. The code retrieves user data based solely on the userId or user_id provided in the URL. It never checks if the currently logged-in user has the permission to view that specific profile. An attacker can change the ID in the URL (e.g., from /account/123 to /account/124) to view private data belonging to any other user.

### **The Fix:**

The secure version of the code validates the identity of the requester against the resource being requested. It ensures users can only access their own data.

**OWASP Reference:** Broken Access Control

## 3 & 4. Cryptographic Failures (A02:2021)

### **Analysis of Snippets 3 & 4**
**The Vulnerability:** Snippet 3 uses MD5, which is cryptographically broken and vulnerable to collision attacks. Snippet 4 uses SHA-1 without a salt. SHA-1 is no longer secure for passwords, and the lack of a salt makes the hashes vulnerable to "Rainbow Table" attacks. If the database is leaked, attackers can instantly reverse these hashes using modern hardware or pre-computed tables to reveal clear-text passwords.

### **The Fix:**

Using Argon2id (the winner of the Password Hashing Competition) provides high resistance to GPU/ASIC cracking. It automatically generates a unique salt for every password.

**OWASP Reference:** Cryptographic Failures

## **5 & 6. Injection (A03:2021)**

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

## **7. Insecure Design (A04:2021)**

### **Analysis of Snippet 7**
**The Vulnerability:** The code snippet allows a password reset solely by providing an email. There is no identity verification (like a token sent via email or an old password check). Any user can change the password of any other user simply by knowing their email address.

### **The Fix:**

The fix moves from a "direct update" to a broken-link workflow. Instead of changing the password immediately, the system generates a cryptographically strong, time-limited token and sends it to the registered email. This ensures that only the person with access to the email account can initiate the reset.

**OWASP Reference:** Insecure Design

## **8. Software and Data Integrity Failures (A08:2021)**

### **Analysis of Snippet 8**
**The Vulnerability:** The code loads a JavaScript library from a third-party Content Delivery Network (CDN) without any integrity verification. If the CDN is compromised or the file is maliciously replaced, the application will blindly execute the attacker's code in the users' browsers.

### **The Fix:**

The fix uses Subresource Integrity (SRI). By adding the integrity attribute with a cryptographic hash of the expected file, the browser will verify the file's contents before executing it. If the file has been tampered with, the hash won't match, and the browser will block the script.

**OWASP Reference:** Software and Data Integrity Failures

## **9. Server-Side Request Forgery (SSRF) (A10:2021)**

### **Analysis of Snippet 9**
**The Vulnerability:** The code snippet accepts a raw URL from user input and immediately performs a GET request from the server. An attacker can provide internal URLs (e.g., http://localhost:8080/admin or http://169.254.169) to access sensitive internal services, metadata, or bypass firewalls that the server has access to but the user does not.

### **The Fix:**

The fix implements an Allowlist. Instead of fetching any URL, the application now verifies that the URL uses the HTTPS protocol and belongs to a predefined list of trusted domains. This prevents the server from being used as a proxy to attack internal infrastructure.

**OWASP Reference:** Server-Side Request Forgery (SSRF)

## **10. Identification and Authentication Failures (A07:2021)**

### **Analysis of Snippet 10**
**The Vulnerability:** The code compares a user-provided password directly to a stored password using a standard equality check. This implies two major failures:
1. Plaintext Storage: It suggests that passwords are stored in plaintext in the database.
2. Timing Attacks: Standard string comparisons can leak information about how many characters matched based on how long the operation takes.

### **The Fix:**

Security is improved by using Cryptographic Hashing (like Argon2 or bcrypt). You should never store or compare raw passwords. The bcrypt.checkpw function is designed to be slow (to thwart brute force) and uses constant-time comparison to prevent timing attacks.

**OWASP Reference:** Identification and Authentication Failures
