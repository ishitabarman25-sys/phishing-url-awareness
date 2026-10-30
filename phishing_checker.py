
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check URL text for selected phishing warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    # Add a scheme if the user did not enter one.
    candidate = url if "://" in url else "http://" + url

    # Handle malformed URL text without crashing.
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: @ symbol
    if "@" in candidate:
        findings.append(
            "Contains an @ symbol; inspect carefully."
        )

    # Check 2: URL longer than 100 characters
    if len(url) > 100:
        findings.append(
            "Unusually long URL (over 100 characters)."
        )

    # Check 3: IPv4-style hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    # Check 4: Five or more hostname segments
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    # Check 5: Punycode marker
    if "xn--" in host:
        findings.append(
            "Contains a punycode-style hostname."
        )

    # Check 6: HTTP scheme
    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    if not findings:
        findings.append(
            "No listed warning signs found. "
            "This does NOT prove safety."
        )

    return findings


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    while True:
        raw_url = input(
            "\nEnter a sample URL (or type q to quit): "
        )

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)

        print("\nResult:")
        for item in findings:
            print("- " + item)

        # Do not count empty or invalid input as phishing warnings.
        informational = (
            "No URL entered.",
            "Could not identify a hostname.",
            "This text is not a valid URL format.",
            "No listed warning signs found."
        )

        if not any(item.startswith(informational) for item in findings):
            print(
                f"\nREVIEW CAREFULLY: "
                f"{len(findings)} warning sign(s) found."
            )

        print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
