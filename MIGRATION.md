# Migration Guide: Dot Numbering Standardization

## Overview

As of this update, Thaibraille now uses the **international standard Braille dot numbering system** to ensure better communication and compatibility with the international Braille community.

## What Changed

### Previous Custom System
- **Left column**: 1 (top), 2 (middle), 5 (bottom)
- **Right column**: 3 (top), 4 (middle), 6 (bottom)
- **8-dot bottom row**: 7 (left), 8 (right)

### New International Standard System
- **Left column**: 1 (top), 2 (middle), 3 (bottom)
- **Right column**: 4 (top), 5 (middle), 6 (bottom)
- **8-dot bottom row**: 7 (left), 8 (right)

This aligns with the ISO/ANSI standard used in EU, UK, US, and the Unicode Braille Patterns block (U+2800-U+28FF).

## Impact on Users

### For End Users
- **No visible changes**: The Braille characters produced are identical
- **Same API**: All function signatures remain unchanged
- **Same output**: `thai_word_braille()` and `thai_text_braille()` produce the same Unicode Braille characters

### For Developers Working with Internal Representations
If you were directly accessing or manipulating the internal dot pattern representations (e.g., in `thai_braille_mapping_dict` or the `Braille` class), you need to be aware of the new numbering:

#### Dot Position Mapping (Old → New)
- Dot 1: unchanged (1 → 1)
- Dot 2: unchanged (2 → 2)
- Dot 3: moved to position 4 (3 → 4)
- Dot 4: moved to position 5 (4 → 5)
- Dot 5: moved to position 3 (5 → 3)
- Dot 6: unchanged (6 → 6)
- Dot 7: unchanged (7 → 7)
- Dot 8: unchanged (8 → 8)

#### Example
- Old pattern `"1234"` → New pattern `"1245"`
- Old pattern `"15"` → New pattern `"13"`
- Old pattern `"156"` → New pattern `"136"`

## Technical Details

The transformation applied to all internal dot patterns follows this mapping:
```
Old numbering: 1, 2, 3, 4, 5, 6, 7, 8
New numbering: 1, 2, 4, 5, 3, 6, 7, 8
```

This ensures that:
1. The physical dot positions match international standards
2. The Unicode Braille Pattern encoding is correctly interpreted
3. Documentation and communication with the international Braille community is clear

## References

- International Braille standard: [Wikipedia - Braille](https://en.wikipedia.org/wiki/Braille)
- Unicode Braille Patterns: [U+2800 to U+28FF](https://unicode.org/charts/PDF/U2800.pdf)
