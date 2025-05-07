#!/usr/bin/env python
"""
Generate a diagram illustrating the standard oddball jitter random protocol.
This script creates a visualization of the different stimulus blocks and their timing.
"""

import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.patches import Rectangle, Circle
from matplotlib.lines import Line2D
import matplotlib.patheffects as path_effects

# Create figure with multiple subplots
fig = plt.figure(figsize=(12, 8))
fig.suptitle('Standard Oddball with Jittered Intervals Protocol', fontsize=16)

# Define colors for different stimulus types
colors = {
    'standard': '#1f77b4',  # blue
    'orientation_deviant': '#ff7f0e',  # orange
    'tf_deviant': '#2ca02c',  # green
    'contrast_deviant': '#d62728',  # red
    'rf_mapping': '#9467bd',  # purple
    'blank': '#7f7f7f',  # gray
}

# 1. Orientation Tuning Component
ax1 = plt.subplot(3, 1, 1)
ax1.set_title('Orientation Tuning Component with Jittered Intervals', fontsize=14)
ax1.set_xlim(0, 20)
ax1.set_ylim(0, 4)
ax1.set_yticks([])
ax1.set_xlabel('Time (s)')

# Create a randomized sequence of orientations and delays
np.random.seed(42)  # For reproducibility
orientations = np.arange(0, 360, 22.5)
delays = [0.343, 1.0, 1.5, 2.0]
stim_duration = 0.343

# Plot orientation stimuli with jittered intervals
current_time = 0
for i in range(12):  # Show a subset of the stimuli
    orientation = np.random.choice(orientations)
    delay = np.random.choice(delays)
    
    # Draw stimulus block - make it taller for better text fitting
    rect = Rectangle((current_time, 0.8), stim_duration, 2.4, 
                     color=colors['standard'], alpha=0.8)
    ax1.add_patch(rect)
    
    # Add orientation text with path effect for better visibility
    text = ax1.text(current_time + stim_duration/2, 2, f"{orientation}°", 
             ha='center', va='center', fontsize=9, color='white')
    text.set_path_effects([path_effects.withStroke(linewidth=1.5, foreground='black')])
    
    # Show delay
    if i < 11:  # Don't show delay after the last stimulus
        ax1.text(current_time + stim_duration + delay/2, 0.5, f"{delay}s", 
                 ha='center', va='center', fontsize=8)
        
        # Draw delay line
        ax1.plot([current_time + stim_duration, current_time + stim_duration + delay], 
                 [0.7, 0.7], 'k-', linewidth=1)
        ax1.plot([current_time + stim_duration, current_time + stim_duration], 
                 [0.5, 0.7], 'k-', linewidth=1)
        ax1.plot([current_time + stim_duration + delay, current_time + stim_duration + delay], 
                 [0.5, 0.7], 'k-', linewidth=1)
    
    current_time += stim_duration + delay

ax1.text(-0.5, 2, "Stimulus\nOrientation", ha='center', va='center', fontsize=10)

# 2. Standard-Oddball Paradigm
ax2 = plt.subplot(3, 1, 2)
ax2.set_title('Standard-Oddball Paradigm with Jittered Intervals', fontsize=14)
ax2.set_xlim(0, 20)
ax2.set_ylim(0, 5)
ax2.set_yticks([])
ax2.set_xlabel('Time (s)')

# Create a sequence with standards and deviants
current_time = 0
stim_types = ['standard'] * 12 + ['orientation_deviant', 'tf_deviant', 'contrast_deviant']
np.random.shuffle(stim_types)
stim_types = stim_types[:16]  # Take a subset for visualization

labels = {
    'standard': '0° (Standard)',
    'orientation_deviant': '45°/90° (Dev)',
    'tf_deviant': '0 Hz (Dev)',
    'contrast_deviant': '0 contrast (Dev)',
}

for i, stim_type in enumerate(stim_types):
    delay = np.random.choice(delays) if i < len(stim_types)-1 else 0
    
    # Draw stimulus block - made taller
    rect = Rectangle((current_time, 0.8), stim_duration, 2.4, 
                     color=colors[stim_type], alpha=0.8)
    ax2.add_patch(rect)
    
    # Add stimulus type text with outline
    text = ax2.text(current_time + stim_duration/2, 2, labels[stim_type], 
             ha='center', va='center', fontsize=7 if stim_type != 'standard' else 8, 
             color='white')
    text.set_path_effects([path_effects.withStroke(linewidth=1.5, foreground='black')])
    
    # Show delay
    if i < len(stim_types) - 1:  # Don't show delay after the last stimulus
        ax2.text(current_time + stim_duration + delay/2, 0.5, f"{delay}s", 
                 ha='center', va='center', fontsize=8)
        
        # Draw delay line
        ax2.plot([current_time + stim_duration, current_time + stim_duration + delay], 
                 [0.7, 0.7], 'k-', linewidth=1)
        ax2.plot([current_time + stim_duration, current_time + stim_duration], 
                 [0.5, 0.7], 'k-', linewidth=1)
        ax2.plot([current_time + stim_duration + delay, current_time + stim_duration + delay], 
                 [0.5, 0.7], 'k-', linewidth=1)
    
    current_time += stim_duration + delay

ax2.text(-0.5, 2, "Stimulus\nType", ha='center', va='center', fontsize=10)

# Add legend for Standard-Oddball
legend_elements = [
    Line2D([0], [0], color=colors['standard'], lw=10, label='Standard (0° orientation)'),
    Line2D([0], [0], color=colors['orientation_deviant'], lw=10, label='Orientation Deviant (45°/90°)'),
    Line2D([0], [0], color=colors['tf_deviant'], lw=10, label='Temporal Frequency Deviant (0 Hz)'),
    Line2D([0], [0], color=colors['contrast_deviant'], lw=10, label='Contrast Deviant (blank screen)'),
]
ax2.legend(handles=legend_elements, loc='upper right', fontsize=8)

# 3. Receptive Field Mapping
ax3 = plt.subplot(3, 1, 3)
ax3.set_title('Receptive Field Mapping', fontsize=14)
ax3.set_xlim(0, 20)
ax3.set_ylim(0, 5)
ax3.set_yticks([])
ax3.set_xlabel('Time (s)')

# Create a visual field grid
grid_size = 5
field_size = 4

# Draw the visual field background
rect = Rectangle((0, 0.5), field_size, field_size, 
                 color='lightgray', alpha=0.3, edgecolor='black')
ax3.add_patch(rect)

# Add text for visual field properties - with background box for better readability
text_box = ax3.text(field_size + 0.5, 2.5, "Small grating properties:\n- 20° diameter\n- 0.08 cpd spatial freq\n- 4 Hz temporal freq\n- 0.8 contrast\n- 250 ms duration\n- 0 ms delay", 
         ha='left', va='center', fontsize=9,
         bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray', boxstyle='round,pad=0.5'))

# Draw sample RF mapping positions
positions = [
    (0.5, 1), (1.5, 1), (2.5, 1), (3.5, 1),
    (0.5, 2), (1.5, 2), (2.5, 2), (3.5, 2),
    (0.5, 3), (1.5, 3), (2.5, 3), (3.5, 3),
    (0.5, 4), (1.5, 4), (2.5, 4), (3.5, 4)
]

# Draw circles representing RF mapping stimuli
for pos in positions:
    circle = Circle((pos[0], pos[1]), 0.25, color=colors['rf_mapping'], alpha=0.7)
    ax3.add_patch(circle)

# Add a sequence representation
current_time = field_size + 6
stim_duration = 0.25  # 250 ms for RF mapping

# Plot some sample RF mapping stimuli in sequence
for i in range(6):
    rect = Rectangle((current_time, 0.8), stim_duration, 2.4, 
                     color=colors['rf_mapping'], alpha=0.8)
    ax3.add_patch(rect)
    
    # No delay between RF stimuli
    current_time += stim_duration

# Add text explanation with background box
text_box2 = ax3.text(field_size + 6 + 3*stim_duration, 2, "Rapid sequence\nNo delays between stimuli", 
         ha='center', va='center', fontsize=9,
         bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray', boxstyle='round,pad=0.5'))

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(hspace=0.4)

# Save the figure
output_dir = '/Users/jerome.lecoq/Documents/Work documents/Allen Institute/Projects/PredictiveProcessingCommunity/openscope-community-predictive-processing/docs/img/stimuli'
output_path = os.path.join(output_dir, 'standard-oddball-jitter-random.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()

print(f"Figure saved to: {output_path}")