#!/usr/bin/env python
"""
Generate a diagram illustrating the sensory-motor closed-loop protocol.
This script creates a visualization of the different stimulus blocks and their relationship to motor activity.
Simplified version showing only open and closed loop conditions.
"""

import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
from matplotlib.lines import Line2D
import matplotlib.patheffects as path_effects

# Create figure with multiple subplots - now with just 2 rows
fig = plt.figure(figsize=(12, 7))
fig.suptitle('Sensory-Motor Closed-Loop Protocol', fontsize=16)

# Define colors for different stimulus types
colors = {
    'standard': '#1f77b4',  # blue
    'orientation_deviant': '#ff7f0e',  # orange
    'tf_deviant': '#2ca02c',  # green
    'contrast_deviant': '#d62728',  # red
    'running': '#9467bd',  # purple
    'not_running': '#7f7f7f',  # gray
    'sensory_motor': '#17becf',  # cyan
    'closed_loop': '#bcbd22',  # yellow
}

# 1. Open-Loop Condition
ax1 = plt.subplot(2, 1, 1)
ax1.set_title('Open-Loop Condition: Standard Oddball Independent of Running', fontsize=14)
ax1.set_xlim(0, 20)
ax1.set_ylim(0, 6)
ax1.set_yticks([])
ax1.set_xlabel('Time (s)')

# Fixed parameters
fixed_delay = 1.0  # 1 second fixed delay
stim_duration = 0.343  # 343 ms stimulus duration

# Create a sequence with standards and deviants
current_time = 0
stim_types = ['standard'] * 5 + ['orientation_deviant'] + ['standard'] * 2 + ['tf_deviant'] + ['standard'] * 2 + ['contrast_deviant'] + ['standard'] * 4

labels = {
    'standard': '0° (Standard)',
    'orientation_deviant': '45° (Deviant)',
    'tf_deviant': '0 Hz (Deviant)',
    'contrast_deviant': '0 contrast (Deviant)',
}

# Running pattern (independent of stimuli)
running_times = []
for i in range(0, 20, 4):
    running_times.extend([(i, i+1.8), (i+2.2, i+3.5)])

# Draw running pattern
for start, end in running_times:
    rect = Rectangle((start, 4), end-start, 1, 
                    color=colors['running'], alpha=0.6)
    ax1.add_patch(rect)
    
# Add running labels with text outline for better visibility
text = ax1.text(10, 4.5, "Running", ha='center', va='center', fontsize=10, color='white')
text.set_path_effects([path_effects.withStroke(linewidth=1.5, foreground='black')])

# Add text with background for better readability
ax1.text(3.5, 5.5, "Running Pattern (independent of stimuli)", 
         ha='center', va='center', fontsize=10,
         bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray', boxstyle='round,pad=0.5'))

# Draw stimuli
for i, stim_type in enumerate(stim_types):
    # Draw stimulus block - made taller for better text fitting
    rect = Rectangle((current_time, 0.8), stim_duration, 2.4, 
                    color=colors[stim_type], alpha=0.8)
    ax1.add_patch(rect)
    
    # Add stimulus type text with outline for better visibility
    text = ax1.text(current_time + stim_duration/2, 2, labels[stim_type], 
            ha='center', va='center', fontsize=7 if stim_type != 'standard' else 8, 
            color='white')
    text.set_path_effects([path_effects.withStroke(linewidth=1.5, foreground='black')])
    
    # Show delay
    if i < len(stim_types) - 1:  # Don't show delay after the last stimulus
        ax1.text(current_time + stim_duration + fixed_delay/2, 0.5, f"{fixed_delay}s", 
                ha='center', va='center', fontsize=8)
        
        # Draw delay line
        ax1.plot([current_time + stim_duration, current_time + stim_duration + fixed_delay], 
                [0.7, 0.7], 'k-', linewidth=1)
        ax1.plot([current_time + stim_duration, current_time + stim_duration], 
                [0.5, 0.7], 'k-', linewidth=1)
        ax1.plot([current_time + stim_duration + fixed_delay, current_time + stim_duration + fixed_delay], 
                [0.5, 0.7], 'k-', linewidth=1)
    
    current_time += stim_duration + fixed_delay

ax1.text(-0.5, 4.5, "Animal\nBehavior", ha='center', va='center', fontsize=10)
ax1.text(-0.5, 2, "Stimulus\nType", ha='center', va='center', fontsize=10)

# Add a cross out symbol to show no connection between running and stimuli
arrow = FancyArrowPatch((6, 3.7), (8, 3.7), arrowstyle='->', mutation_scale=15, 
                        linestyle='--', color='red', linewidth=1)
ax1.add_patch(arrow)
ax1.text(7, 3.7, "×", color='red', fontsize=20, ha='center', va='center')

# 2. Closed Loop: Running-Triggered Oddball
ax2 = plt.subplot(2, 1, 2)
ax2.set_title('Closed Loop: Running State Determines Stimulus Type', fontsize=14)
ax2.set_xlim(0, 20)
ax2.set_ylim(0, 6)
ax2.set_yticks([])
ax2.set_xlabel('Time (s)')

# Draw running pattern
for start, end in running_times:
    rect = Rectangle((start, 4), end-start, 1, 
                    color=colors['running'], alpha=0.6)
    ax2.add_patch(rect)

    # Draw corresponding deviant stimulus during running
    if end-start > 0.5:  # Only if running period is long enough
        mid_point = (start + end) / 2
        if mid_point < 20 - stim_duration:
            rect = Rectangle((mid_point, 0.8), stim_duration, 2.4, 
                            color=colors['orientation_deviant'], alpha=0.8)
            ax2.add_patch(rect)
            text = ax2.text(mid_point + stim_duration/2, 2, "Deviant\nTrigger", 
                    ha='center', va='center', fontsize=8, color='white')
            text.set_path_effects([path_effects.withStroke(linewidth=1.5, foreground='black')])
            
            # Draw connection arrow
            arrow = FancyArrowPatch((mid_point + stim_duration/2, 4), 
                                   (mid_point + stim_duration/2, 3), 
                                   arrowstyle='->', mutation_scale=15, color='black')
            ax2.add_patch(arrow)

# Draw standard stimuli during non-running periods
current_time = 0
non_running = []
for i in range(len(running_times)):
    if i == 0:
        if running_times[i][0] > 0:
            non_running.append((0, running_times[i][0]))
    else:
        non_running.append((running_times[i-1][1], running_times[i][0]))
    
    if i == len(running_times) - 1 and running_times[i][1] < 20:
        non_running.append((running_times[i][1], 20))

# Draw non-running
for start, end in non_running:
    rect = Rectangle((start, 4), end-start, 1, 
                    color=colors['not_running'], alpha=0.4)
    ax2.add_patch(rect)
    
    # Add standard stimulus during non-running (if period is long enough)
    if end - start > stim_duration + 0.3:
        mid_point = (start + end) / 2
        rect = Rectangle((mid_point, 0.8), stim_duration, 2.4, 
                        color=colors['standard'], alpha=0.8)
        ax2.add_patch(rect)
        text = ax2.text(mid_point + stim_duration/2, 2, "Standard", 
                ha='center', va='center', fontsize=8, color='white')
        text.set_path_effects([path_effects.withStroke(linewidth=1.5, foreground='black')])
                
        # Draw connection arrow
        arrow = FancyArrowPatch((mid_point + stim_duration/2, 4), 
                               (mid_point + stim_duration/2, 3), 
                               arrowstyle='->', mutation_scale=15, color='black')
        ax2.add_patch(arrow)

# Add running labels with text outline for better visibility
text1 = ax2.text(3, 4.5, "Running", ha='center', va='center', fontsize=9, color='white')
text1.set_path_effects([path_effects.withStroke(linewidth=1.5, foreground='black')])
text2 = ax2.text(16, 4.5, "Not Running", ha='center', va='center', fontsize=9)
text2.set_path_effects([path_effects.withStroke(linewidth=1, foreground='gray')])

ax2.text(-0.5, 4.5, "Animal\nBehavior", ha='center', va='center', fontsize=10)
ax2.text(-0.5, 2, "Stimulus\nType", ha='center', va='center', fontsize=10)

# Add connection text with background box for better readability
ax2.text(10, 5.5, "Running state triggers deviants, non-running triggers standards", 
        ha='center', va='center', fontsize=10, 
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.5'))

# Add a simple explanatory box at the bottom
ax2.text(10, 0.2, "This closed-loop paradigm creates a predictable relationship between the animal's\nrunning behavior and the visual stimuli, allowing for studies of prediction error signals.", 
        ha='center', va='center', fontsize=10,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.5'))

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(hspace=0.4)

# Save the figure
output_dir = '/Users/jerome.lecoq/Documents/Work documents/Allen Institute/Projects/PredictiveProcessingCommunity/openscope-community-predictive-processing/docs/img/stimuli'
output_path = os.path.join(output_dir, 'sensory-motor-closed-loop.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()

print(f"Figure saved to: {output_path}")