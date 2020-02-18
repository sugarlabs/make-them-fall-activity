What is this?
=============

Make Them Fall is a multilevel arcade game for the Sugar desktop.

How to use?
===========

Make Them Fall is part of the Sugar desktop.  Please refer to;

* [How to Get Sugar on sugarlabs.org](https://sugarlabs.org/),
* [How to use Sugar](https://help.sugarlabs.org/),
* [Download Make Them Fall using Browse](https://activities.sugarlabs.org/), search for `Make Them Fall`, then download, and;
* Refer the 'How to play' section inside the activity

How to upgrade?
===============

On Sugar desktop systems;
* use [My Settings](https://help.sugarlabs.org/my_settings.html), [Software Update](https://help.sugarlabs.org/my_settings.html#software-update), or;
* use Browse to open [activities.sugarlabs.org](https://activities.sugarlabs.org/), search for `Make Them Fall`, then download.

How to run?
=================

Make Them Fall depends on Python, PyGTK and PyGame.

Make Them Fall is started by [Sugar](https://github.com/sugarlabs/sugar).

Make Them Fall is not packaged by Debian, Ubuntu and Fedora distributions.  
On Ubuntu and Debian systems these required dependencies (`python-gtk2-dev` and
`python-pygame`) need to be manually installed.
On Fedora system these dependencies (`pygtk2` and `pygame`) need to be manually installed.


**Running outside Sugar**


- Install the dependencies - 

On Debian and Ubuntu systems;

```
sudo apt install python-gtk2-dev python-pygame
```

On Fedora systems;

```
sudo dnf install pygtk2 pygame
```

- Clone the repo and run-
```
git clone https://github.com/sugarlabs/make-them-fall-activity.git
cd make-them-fall-activity
python main.py
```

**Running inside Sugar**

- Open Terminal activity and change to the Make Them Fall activity directory
```
cd activities\MakeThemFall.activity
```
- To run
```
sugar-activity .
```
