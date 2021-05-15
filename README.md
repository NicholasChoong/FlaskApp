# PC wiki

## Setup

flask db init
flask db migrate
flask db upgrade

## Testing

python test.py
flask shell

## Planned contents

CPU

    Connected though main socket

    Depends on manufacturer and model

GPU

    Connects through a PCI-E connection

    Commonly uses PCI-E 3.0 but modern cards are now supporting 4.0

RAM

    Operates in DDR (Double Data Rate)

    To use this mode installed in pairs

    Speed and max size are determined by the CPU and motherboard

Storage Drive

    Connected through SATA, or M.2

    Can be SSD or HDD.

Fan/Liquid Cooling

    Necessary for ensuring a computer continued operation

PSU

    Bringer of power to the system

    Power Efficiency

Case

    I/O

    USB

    Ethernet

    Power/ Reset buttons

    Audio jacks

Peripherals

    Keyboard

    Switches

    Mouse

    DPI

    Monitor

    Resolution

    Contrast Ratio

    Refresh rate

    Response time

    Webcam

    Megapixels

    Speakers/Headset/Earphone

    Speaker range

    Mic

Global

Navigation bar

    Home

    Lessons

    Assessments

Login info

Dark Mode

Planned Pages

1. Home Page

2. Lessons Page

3. Assessments Page

    ```
    HTML Form

    Marking done on server-side
    ```

4. Login page

    ```
    Login and signup
    ```

5. Administrative page

    ```
    Administrative information (not visible to non admin users)

    Secure access
    ```

6. Review page

# Table Models

![Entity Relationship Diagrams](./ERD.png)
