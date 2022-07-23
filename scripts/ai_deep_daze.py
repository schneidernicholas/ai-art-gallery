# Deep Daze AI Imagine
# Run batches of AI generation
# Copyright (C) 2022: Nicholas Schneider
# Licensed under MIT: https://github.com/schneidernicholas/ai-art-gallery/tree/main/scripts/LICENSE.md

# Usage: python ai_deep_daze.py
# See https://github.com/lucidrains/deep-daze for the deep_daze required library

from deep_daze import Imagine

mind = [
    "Planet Earth",
#   "Cosmos and Earth", # Comment out a line like this to make it inactive.
    "Jazz",
    "Cosmos in the style of Van Gogh",
    "Jazz|The Universe", # Multiple phrases can be generated into one image by separating with a | delimiter
];

for thought in mind:
    imagine = Imagine(
        text = thought,
        save_every = 1050, # How often (epochs) to save progress if save_progress is True
        save_progress = True, # Set this to True if you want each progress at each iteration to be saved as a PNG (can take a lot of disk space)
        iterations = 1050,
        save_date_time = True
    )

    imagine();


""" Defaults:
Imagine(
    self,
    clip_perceptor,
    clip_norm,
    input_res,
    total_batches,
    batch_size,
    num_layers=8,
    image_width=512,
    loss_coef=100,
    theta_initial=None,
    theta_hidden=None,
    lower_bound_cutout=0.1, # should be smaller than 0.8
    upper_bound_cutout=1.0,
    saturate_bound=False,
    gauss_sampling=False,
    gauss_mean=0.6,
    gauss_std=0.2,
    do_cutout=True,
    center_bias=False,
    center_focus=2,
    hidden_size=256,
    averaging_weight=0.3,
):
"""
