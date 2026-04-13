## **1. Broken Access Control (A01:2021)**

### **Security Flaw:**
The vulnerable code sample is an Insecure Direct Object Reference (IDOR). The application takes a user_id directly from the URL and fetches the data without checking if the currently logged-in user has permission to view that specific account. An attacker could simply change the ID in the URL to view any user's private data.

### **Explanation of Fix**
The fix implements an access control check. By comparing the requested user_id against the current_user.id from the secure session, we ensure users can only access their own records. Using @login_required also ensures that unauthenticated "anonymous" users cannot hit the endpoint.

### **References**
OWASP: Broken Access Control

## 2. Cryptographic Failures (A02:2021)

### **Security Flaw:**
The code sample uses MD5, a cryptographically broken hashing algorithm. MD5 is highly susceptible to collision attacks and can be "cracked" almost instantly using rainbow tables or modern hardware. Furthermore, the code lacks a salt, making it vulnerable to pre-computed dictionary attacks.

### **Explanation of Fix**
The fix replaces MD5 with BCrypt, a strong, adaptive hashing algorithm recommended by OWASP.

### **References**
OWASP: Cryptographic Failures
