from libqtile import layout
from libqtile.config import Match

layouts = [
    layout.MonadTall(margin=10, single_margin=10, border_focus='#5294e2', border_width=1, ratio=0.6),
    layout.Columns(margin=10, border_focus='#5294e2', border_normal='#2c5380',border_width=1,),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(margin=6, border_focus='#5294e2', border_normal='#2c5380', ratio='1.6'),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(expand=False, margin=10, master_match='Firefox', border_focus='#5294e2', border_normal='#2c5380'),
    layout.TreeTab(margin=10),
    # layout.VerticalTile(),
    # layout.Zoomy(columnwidth=600, margin=10, property_small='0.5'),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
]
)
