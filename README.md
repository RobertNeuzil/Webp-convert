# Webp-convert


```text
  ┌──────────────────┐
  │  INPUT FORMATS   │
  │                  │
  │  .png   .jpeg    │
  │  .jpg   .bmp     │   ═══════╗
  │  .tiff  .tif     │          ║
  │  .gif            │          ║
  └──────────────────┘          ▼
                        ┌──────────────┐
                        │  CONVERTING  │
                        └──────────────┘
                                ║
                                ║
                                ▼
                       ┌────────────────┐
                       │  OUTPUT IMAGE  │
                       │                │
                       │     .webp      │
                       └────────────────┘
```


Webp is now the superior file format. Converting old images manually is time consuming.

Now you have a py script to batch them

I have tried logging error messages in terminal but with photo conversions there can always be potential hang ups that will crash python.
I suggest running in bash to force window open until everything convert cleanly or you trace the source of the problematic file / directory

