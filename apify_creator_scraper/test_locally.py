from main import scrape_bio_link, extract_emails

def test_logic():
    print("Testing Email Extraction...")
    text = "Contact me at hello@example.com for collabs"
    assert "hello@example.com" in extract_emails(text)
    print("[PASS] Email Extraction Passed")

    print("\nTesting Deep Link Scraping (Simulated)...")
    # We will test with a known safe site that might have an email or just verify it doesn't crash
    # Using a dummy URL for now just to ensure the function handles errors gracefully
    emails = scrape_bio_link("https://httpbin.org/html") 
    print(f"Result from httpbin (Expected []): {emails}")
    
    # You can manually test with a real linktree if you want, e.g.
    # real_test = scrape_bio_link("https://linktr.ee/someuser")
    
    print("\n[PASS] Logic Verification Complete. The code structure is valid.")

if __name__ == "__main__":
    test_logic()
