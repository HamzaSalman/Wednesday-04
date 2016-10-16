# Created by: Hamza Salman
# Created on: September 2016
# Created for: ICS3U
# This program has multiple files which it switches through when it is played.

from scene import *
import ui

from splash_scene import *


main_view = ui.View()
scene_view = SceneView(frame = main_view.bounds, flex = 'WH')
main_view.add_subview(scene_view)
scene_view.scene = SplashScene()
main_view.present(hide_title_bar = True, animated = False)
