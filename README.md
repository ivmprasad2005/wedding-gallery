# Teja Digitals — Live Event Photo Gallery Platform

A full-stack web application built for a photography studio to manage and share event photos in real time. Photographers upload photos through an admin dashboard, and customers access a live, auto-updating gallery via a unique QR code — no app installation required.

🔗 **Live Demo:** [wedding-gallery-jdvx.onrender.com/admin.html](https://wedding-gallery-jdvx.onrender.com/admin.html)

## Features

- 📤 **Multi-file photo upload** with real-time progress tracking
- 🗂️ **Event-based organization** — each customer/event gets its own isolated gallery
- 📱 **Live-updating gallery** — new photos appear automatically without refreshing
- 🔍 **Zoom & quality check** — scroll/pinch to inspect photo details before sharing
- ⬇️ **One-click photo download** for customers
- 🧾 **Dynamic QR code generation** — instantly create a shareable gallery link per event
- 🗑️ **Delete controls** — remove individual photos or entire events
- ☁️ **Persistent cloud storage** via Cloudinary — zero data loss across deployments
- 🎨 **Custom branding** — studio banner, color theme, and logo integration

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI |
| Frontend | HTML, CSS, JavaScript (vanilla) |
| Storage | Cloudinary (cloud image storage) |
| Deployment | Render (CI/CD via GitHub) |
| Version Control | Git, GitHub |

## How It Works

1. **Admin Dashboard** (`admin.html`) — view all events, create new ones, generate QR codes
2. **Upload Panel** (`uploads.html`) — photographer uploads multiple photos per event
3. **Customer Gallery** (`gallery.html`) — guests scan a QR code to view and download photos live, as they're uploaded

## Architecture
Browser (Upload) → FastAPI Backend → Cloudinary (Storage)
Browser (Gallery) ← FastAPI Backend ← Cloudinary (Storage)


Photos are stored in Cloudinary under event-specific folders, decoupling media storage from the application server for reliability and persistence.

Built as a self-directed learning project — from zero prior web development experience to a deployed, production-ready application.