#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
WHITELIST - Simple Test Script
This script displays messages in both Persian and English in CMD
"""

import sys
import os

# Clear screen for better visibility
os.system('cls' if os.name == 'nt' else 'clear')

# Persian messages with box design
print("=" * 60)
print("🛡️  WHITELIST - اسکریپت تست ساده")
print("=" * 60)
print()

print("📌 پیام‌های فارسی:")
print("-" * 40)
print("هیچ چیز خاصی در این اسکریپت وجود ندارد.")
print()

print("📌 English Messages:")
print("-" * 40)
print("There is nothing special in this script.")
print()

print("=" * 60)
print("✨ هیچی نیست! | Nothing here!")
print("=" * 60)

# Wait for user input before closing (optional)
input("\nPress Enter to exit...")
