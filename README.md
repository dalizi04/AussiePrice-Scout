Project: AussiePrice Scout 🛒
An automated data pipeline to track, translate, and compare grocery prices across major Australian supermarkets (Coles, Woolworths, Aldi).

🙏 Acknowledgements
Special thanks to the Grocermatic project for providing the comprehensive raw grocery data. Their commitment to open-source pricing transparency is the foundation of this project.

⚠️ Known Issues & Limitations
Unit Inconsistency: Currently, the system compares products based on their total retail price rather than unit price (e.g., price per kg/L).

Example: "Chicken Drumsticks" may show as $7.50 (for a 1.5kg pack) vs. $0.72 (for a single unit or 100g price).

Translation Limits: Due to free API rate limiting, translations for 24k+ items are processed in batches with a local caching mechanism to optimize performance.
