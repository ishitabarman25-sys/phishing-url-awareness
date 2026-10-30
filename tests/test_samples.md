# Phishing URL Awareness – Test Samples

## Objective
To test the phishing URL checker using different types of URLs and observe the warning signs detected by the program.

## Test Case 1: Trusted Website

**Input:**
`https://www.google.com`

**Expected Result:**
The URL should be identified as a potentially safe website, subject to the checks implemented in the program.

## Test Case 2: HTTP Website

**Input:**
`http://example.com`

**Expected Result:**
The program may identify the absence of HTTPS as a warning sign.

## Test Case 3: IP Address URL

**Input:**
`http://192.0.2.10/account`

**Expected Result:**
The program should identify an IP-address-based hostname as a potential warning sign.

## Test Case 4: Suspicious URL

**Input:**
`http://secure-login-example.tk/account/verify`

**Expected Result:**
The program should check for suspicious URL characteristics such as unusual domain extensions, misleading keywords, and HTTP usage.

## Test Case 5: Program Exit

**Input:**
`q`

**Expected Result:**
The program should terminate and display a goodbye message.
## Actual Test Results

| Test Case | Input URL | Actual Warning Count | Status |
|---|---|---|---|
| IP Address URL | `http://192.0.2.10/account` | 2 | Passed |
| Suspicious-looking URL | `http://secure-login-example.tk/account/verify` | 1 | Passed |
| Familiar HTTPS Website | `https://www.google.com` | 0 | Passed |

### Test Summary

The phishing URL checker was executed using three different URL patterns. It detected two warning signs for the IP-address-based URL, one warning sign for the suspicious-looking URL, and no listed warning signs for the familiar HTTPS website.

The results demonstrate the basic functionality of the URL analysis program. However, the absence of warning signs does not guarantee that a website is safe.
## Conclusion

The test samples help evaluate the URL checker against different URL patterns. The results depend on the detection rules implemented in the Python program.
