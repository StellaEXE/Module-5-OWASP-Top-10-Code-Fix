## **1. Broken Access Control (A01:2021)**

### **Security Flaw:**

This code demonstrates an Insecure Direct Object Reference (IDOR). The endpoint retrieves account information based solely on a user_id provided in the URL. There is no logic to verify if the requester is the owner of the account or an authorized admin. An attacker could iterate through IDs (e.g., /account/1, /account/2) to scrape sensitive data from all users.

### **Explanation of Fix**
The fix implements an access control check. By comparing the requested user_id against the current_user.id from the secure session, we ensure users can only access their own records. Using @login_required also ensures that unauthenticated "anonymous" users cannot hit the endpoint.

### **References**

OWASP: Broken Access Control

## 2. A02:2021 – Cryptographic Failures
