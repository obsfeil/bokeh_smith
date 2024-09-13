from bokeh.io import show, output_notebook
from bokeh.plotting import figure
import numpy as np

output_notebook()

# Sett opp en bokeh-figur
p = figure(width=500, height=500, title="Smith Chart", x_range=(-1.2, 1.2), y_range=(-1.2, 1.2))

# Tegn enhetssirkelen
p.annular_wedge(x=0, y=0, inner_radius=1, outer_radius=1, start_angle=0, end_angle=2*np.pi, 
                fill_color=None, line_color="black", line_dash="dashed")

# Tegn flere sirkler som linjer for refleksjonskoeffisienter
radii = np.linspace(0, 1, 11)
for r in radii:
    p.annular_wedge(x=0, y=0, inner_radius=r, outer_radius=r, start_angle=0, end_angle=2*np.pi, 
                    fill_color=None, line_color="blue", alpha=0.5, line_dash="dashed")

# Tegn en linje som eksempel (s11-linje)
s11 = np.linspace(1, 0.8, 10) * np.exp(2 * np.pi * 1j * np.linspace(0, 0.1, 10))
p.scatter(s11.real, s11.imag, size=10, color="red")

# Tilpass akseetiketter og grid
p.xaxis.axis_label = "Re(Z)"
p.yaxis.axis_label = "Im(Z)"
p.grid.visible = True

# Vis grafen
show(p)
