# Mobility-VLA-Auto-Narration
Mobility VLA with Auto-Narration Capabilities

So far: 
1. Blender scene: kitchen_scene.blend.zip. Made with imported objects from blenderkit, I placed them in the scene to make an obstacle course.
2. Assets: Unzip to find:
	- cam_locs: Extracted camera locations by using save_cam_locs.py. Note you have to select active camera then run that script in blender.
	- Video walkthrough: MP4
3. save_cam_locs.py:  Note you have to select active camera then run that script in blender to save cam locations and rotation for each frame.
4. topological_graph: reads in the camera locations, generates frames from the MP4, and creates the topological graph with the relevant data for each frame. It will connect all subsequent frames, and also frames whose distances are less than a user-settable epsilon parameter.