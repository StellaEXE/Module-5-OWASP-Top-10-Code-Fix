## **1. Broken Access Control (A01:2021)**

This category involves failures in restricting what authenticated users can do or see.

### **Analysis of Snippets 1 & 2**
**The Flaw:** Both snippets suffer from an Insecure Direct Object Reference (IDOR) vulnerability. The code retrieves user data based solely on the userId or user_id provided in the URL. It never checks if the currently logged-in user has the permission to view that specific profile.

**Security Risk:** An attacker can change the ID in the URL (e.g., from /account/123 to /account/124) to view private data belonging to any other user.

### **The Fix:**

The secure version of the code validates the identity of the requester against the resource being requested. It ensures users can only access their own data.

**OWASP Reference:** Broken Access Control

## 2. Cryptographic Failures (A02:2021)

This involves the use of weak or insecure cryptographic practices, often leading to sensitive data exposure.

### **Analysis of Snippets 3 & 4**
**The Flaw:** Snippet 3 uses MD5, which is cryptographically broken and vulnerable to collision attacks. Snippet 4 uses SHA-1 without a salt. SHA-1 is no longer secure for passwords, and the lack of a salt makes the hashes vulnerable to "Rainbow Table" attacks.

**Security Risk:** If the database is leaked, attackers can instantly reverse these hashes using modern hardware or pre-computed tables to reveal clear-text passwords.

### **The Fix:**

Using Argon2id (the winner of the Password Hashing Competition) provides high resistance to GPU/ASIC cracking. It automatically generates a unique salt for every password.

**OWASP Reference:** Cryptographic Failures
