# Chapter 2: Robotics Fundamentals 

This chapter delves into the foundational aspects of robotics, exploring the physical anatomy, diverse types, and kinematic principles essential for understanding physical AI and humanoid robotics.

## 1. Robotics Anatomy and Components

A robot is a complex system integrating various components to perceive, process, and act upon its environment. Understanding these core anatomical parts is crucial for designing and analyzing robotic systems.

*   **Manipulator/Body:** The physical structure of the robot, often comprising a series of rigid links connected by joints. This forms the kinematic chain that enables movement and interaction with the environment. For humanoid robots, this includes a torso, limbs, and a head.
*   **End-Effector:** The tool or device attached to the end of a robot's arm (manipulator) that interacts directly with the environment. Examples include grippers, welding torches, cameras, or specialized instruments. Its design is task-specific.
*   **Actuators:** Devices responsible for converting electrical, hydraulic, or pneumatic energy into mechanical motion, thereby driving the robot's joints. Common types include electric motors (DC, AC, stepper, servo), hydraulic cylinders, and pneumatic cylinders. The choice of actuator impacts speed, strength, and precision.
*   **Sensors:** Devices that allow the robot to perceive its internal state and external environment. These provide feedback to the control system. Key sensor types include:
    *   **Proprioceptive Sensors:** Measure internal states like joint angles (encoders, potentiometers), forces/torques (force-torque sensors), and velocities.
    *   **Exteroceptive Sensors:** Measure external environmental properties, such as distance (LiDAR, ultrasonic, radar), vision (cameras), touch (tactile sensors), and proximity.
*   **Controller:** The "brain" of the robot, typically a computer or microcontroller, that processes sensor data, executes algorithms, and sends commands to the actuators to achieve desired movements or tasks. Modern controllers often incorporate advanced AI and machine learning algorithms for perception, decision-making, and motor control.
*   **Power Supply:** Provides the necessary energy to operate all robot components, often batteries for mobile robots or direct current/alternating current for industrial robots.

## 2. Types of Robots

Robots are broadly categorized based on their application, form factor, and operational environment. While classifications can overlap, several distinct types are prominent.

*   **Industrial Robots:** Designed for manufacturing environments, performing repetitive, high-precision tasks such as welding, painting, assembly, material handling, and palletizing. They are typically stationary, robust, and operate within caged environments for safety. Examples include articulated robots, SCARA robots, and gantry robots.
*   **Service Robots:** Assist humans in various non-manufacturing settings, both professional and personal. This category is vast and includes:
    *   **Professional Service Robots:** Operate in hospitals (surgical assistants, delivery robots), logistics (warehouse AGVs/AMRs), agriculture (harvesting robots), and exploration (ROVs, UAVs).
    *   **Personal Service Robots:** Used in homes for tasks like vacuuming, lawn mowing, elder care assistance, and entertainment.
*   **Humanoid Robots:** Mimic the human body form, possessing a torso, head, two arms, and two legs. Their design aims for interaction with human-centric environments and tasks. Research in humanoid robotics focuses on bipedal locomotion, human-robot interaction, manipulation, and advanced AI for complex decision-making and learning. Examples include Boston Dynamics' Atlas and Honda's ASIMO.
*   **Mobile Robots:** Capable of moving autonomously or semi-autonomously in an environment. They include wheeled, tracked, and legged robots, used for exploration, surveillance, delivery, and various service tasks. Navigational capabilities, mapping, and obstacle avoidance are key challenges.
*   **Collaborative Robots (Cobots):** Designed to work safely alongside humans in shared workspaces without physical barriers. They often have force/torque sensors and advanced safety features to prevent harm. Cobots are increasingly used in assembly and quality inspection tasks.

## 3. Degrees of Freedom and Joints

**Degrees of Freedom (DoF)** refer to the number of independent parameters that define the configuration of a mechanical system. In robotics, it typically refers to the number of independent movements a robot's joints can make, which directly impacts its dexterity and workspace.

*   **Translational DoF:** Movement along an axis (e.g., x, y, z). A free object in 3D space has 3 translational DoF.
*   **Rotational DoF:** Rotation about an axis (e.g., roll, pitch, yaw). A free object in 3D space has 3 rotational DoF.

A rigid body in 3D space has 6 DoF (3 translational, 3 rotational). A robot's total DoF is the sum of the DoF of its individual joints.

**Joints** are the connections between rigid links in a robot's kinematic chain, allowing relative motion between them. They are the primary source of a robot's DoF.

*   **Revolute (Rotational) Joint (R-joint or Prismatic Joint):** Allows relative rotation between two links about a single axis. This is the most common type in articulated robot arms, mimicking biological joints like elbows or shoulders. Each revolute joint contributes 1 DoF.
*   **Prismatic (Linear) Joint (P-joint or Slider Joint):** Allows relative linear motion (translation) along a single axis between two links. These are often found in gantry robots or for extending/retracting linear segments. Each prismatic joint contributes 1 DoF.

More complex joints can combine these motions (e.g., cylindrical, spherical), contributing more DoF. The number and type of joints dictate a robot's reach, manipulability, and ability to perform intricate tasks. For instance, a robot with 6 DoF (typically 6 revolute joints) can reach any point in its workspace with any orientation, making it highly versatile for many industrial and advanced robotic applications.