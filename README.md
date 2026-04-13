# Module-5-OWASP-Top-10-Code-Fix

## **1. A01:2021 – Broken Access Control**

### **Security Flaw:**

This code demonstrates an Insecure Direct Object Reference (IDOR). The endpoint retrieves account information based solely on a user_id provided in the URL. There is no logic to verify if the requester is the owner of the account or an authorized admin. An attacker could iterate through IDs (e.g., /account/1, /account/2) to scrape sensitive data from all users.

### **How the fix addresses the vulnerability**

**Authentication:** The @login_required decorator ensures the user is identified.

**Authorization Check:** It explicitly compares the current_user.id from the session with the requested user_id. If they don’t match, it returns a 403 Forbidden error, enforcing proper access control.

**OWASP Reference:** A01:2021-Broken Access Control
