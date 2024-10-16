# meta tag og_extractor
Open Graph Protocol Data Extractor

## Overview

The Open Graph Data Extractor API is a Django-based service that allows users to extract Open Graph metadata from any webpage. By accessing the endpoint `https://og-extractor.vercel.app/og?url=<webpageurl>`, users can retrieve relevant OG tags and associated information.

## Features

- Extract Open Graph metadata from any given URL.
- Returns relevant information such as title, description, and image URL.


# Example of extracting OG data
curl -X GET "https://og-extractor.vercel.app/og?url=<https://example.com>" 

# Read More About Open Graph Protocols
https://ogp.me/
