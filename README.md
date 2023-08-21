# Conway's Game of Life

A simple Python/Tk implementation of [Conway's Game of Life][cgl].  The world
state is randomly seeded, and it does not yet support interactive intervention.

## Development

A functional Python/Tk installation is required. Unsusually for Python packages,
the easiest way to install Tk actually seems to be using a system package
installer and not `pip`.  The [recommended][at] solution is to use an ActiveTcl
installer.

However, MacPorts has a functional distribution, and since it is my preferred
system package manager:

```
port install -vc py310-tkinter tk +quartz
```

With that, no other packages need to be installed.

[cgl]: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
[at]: https://tkdocs.com/tutorial/install.html
[mp]: https://macports.org/
