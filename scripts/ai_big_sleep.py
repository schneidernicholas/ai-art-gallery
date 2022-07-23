# Big Sleep AI Dream
# Run batches of AI generation
# Copyright (C) 2022: Nicholas Schneider
# Licensed under MIT: https://github.com/schneidernicholas/ai-art-gallery/tree/main/scripts/LICENSE.md

# Usage: python ai_big_sleep.py
# See https://github.com/lucidrains/big-sleep for the big_sleep required library

from big_sleep import Imagine

mind = [
    "The Universe in the style of Da Vinci",
#   "Cosmos and Earth", # Comment out a line like this to make it inactive.
    "The Universe|Aliens", # Multiple phrases can be generated into one image by separating with a | delimiter
    "An alien eating ice cream",
];

for thought in mind:
    dream = Imagine(
        text = thought,
        save_every = 2, # How often to save progress if save_progress is True
        save_progress = True, # Set this to True if you want each progress at each iteration to be saved as a PNG (can take a lot of disk space)
        append_seed = True
    );

    dream();


""" Default values:
Imagine(
    self,
    *,
    text=None,
    img=None,
    encoding=None,
    text_min = "",
    lr = .07,
    image_size = 512,
    gradient_accumulate_every = 1,
    save_every = 50,
    epochs = 20,
    iterations = 1050,
    save_progress = False,
    bilinear = False,
    open_folder = True,
    seed = None,
    append_seed = False,
    torch_deterministic = False,
    max_classes = None,
    class_temperature = 2.,
    save_date_time = False,
    save_best = False,
    experimental_resample = False,
    ema_decay = 0.99,
    num_cutouts = 128,
    center_bias = False
);
"""
