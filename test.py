from robot_io.input_devices.vr_input import VrInput

def main():

    # recorder = hydra.utils.instantiate(cfg.recorder)
    # robot = hydra.utils.instantiate(cfg.robot)
    # env = hydra.utils.instantiate(cfg.env, robot=robot)
    # obs = env.reset()
    # input_device = hydra.utils.instantiate(cfg.input, robot=robot)
    # workspace_limits = [[0.3, -0.5, 0.05], [0.6, 0.5, 0.5]]  # [x, y, z, rot_x, rot_y, rot_z]
    workspace_limits = [[-10, -10, 0.0], [10, 10, 2]]  # [x, y, z, rot_x, rot_y, rot_z]
    
    input_device = VrInput(robot=None, 
                           button_hold_threshold=60, 
                           workspace_limits=workspace_limits, 
                           tracking_error_threshold=0.05)

    while True:
        action, record_info = input_device.get_action()
        # print(action)
        # next_obs, _, _, _ = env.step(action)
        # recorder.step(action, obs, record_info)
        # env.render()
        # obs = next_obs

if __name__ == "__main__":
    main()