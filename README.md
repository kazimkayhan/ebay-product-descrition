# eBay Product Description Template

One self-contained folder for product uploaders: **HTML template**, **CSS**, and **all assets** (logos, images). Use it as the base for product descriptions; replace placeholders with your own keys/values when integrating with your upload flow.

## Contents

```
ebay-template/
├── index.html              # Full product description (example: Bremsbeläge VW Golf VII)
├── README.md               # This file
└── assets/
    ├── style/
    │   └── style.css       # All template styles
    └── image/
        ├── logo.webp       # Logo
        ├── logo.svg
        ├── car.webp        # Hero (desktop)
        ├── car-mobile.webp # Hero (mobile)
        ├── about-us.webp   # Footer contact
        ├── shop.svg
        ├── category.svg
        ├── message-text.svg
        └── messages-2.svg
```

## Design and content

- **Design** matches the sample product description (header, hero, cards, tabs, footer).
- **Content** is real example data (no `$ { PRODUCT.* }` placeholders): one product example (Bremsbeläge VW Golf VII), Autoteile-Stark.de contact and legal text. You can later plug in your own variable names and data source.

## Before production (e.g. S3)

1. **Upload this folder** to your storage (e.g. S3): keep the same structure so that `index.html` and `assets/` are in the same place (or adjust paths as below).
2. **Asset URLs**: The HTML uses **relative** paths (`assets/style/style.css`, `assets/image/logo.webp`, etc.).  
   - If you serve the HTML and assets from the **same origin/path** (e.g. `https://your-cdn.com/ebay-template/index.html` and `https://your-cdn.com/ebay-template/assets/...`), relative paths work as-is.  
   - If you host assets on a **different domain/path** (e.g. S3 bucket or CDN), replace the path prefix in the HTML (e.g. find `assets/` and replace with `https://your-bucket.s3.amazonaws.com/ebay-template/assets/` or your final base URL).
3. **Product-specific data**: Replace the example product title, description, compatibility, images, safety text, etc. with your own fields/keys when wiring to your product uploaders.

## Local preview

Open `index.html` in a browser from the folder (file:// or a local server). All links are relative, so it will work as long as `assets/` sits next to `index.html`.

## Tabs

Tabs (Beschreibung, Kompatibilität, Rückgabe, SICHERHEITSINFORMATIONEN, Hersteller Information) are switched with a small inline script at the bottom of `index.html`. You can remove or replace it if your environment injects the description differently.
