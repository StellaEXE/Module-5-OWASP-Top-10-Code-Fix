# Module-5-OWASP-Top-10-Code-Fix

## **1. A01:2021 – Broken Access Control**
**Security Flaw:** This code demonstrates an Insecure Direct Object Reference (IDOR). The endpoint retrieves account information based solely on a user_id provided in the URL. There is no logic to verify if the requester is the owner of the account or an authorized admin. An attacker could iterate through IDs (e.g., /account/1, /account/2) to scrape sensitive data from all users.

