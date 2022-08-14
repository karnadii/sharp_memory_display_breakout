import board
import busio
import displayio
import framebufferio
import sharpdisplay
displayio.release_displays()
chip_select_pin = board.P0_03
bus = board.SPI()
framebuffer = sharpdisplay.SharpMemoryFramebuffer(bus, chip_select_pin, 160, 68)
display = framebufferio.FramebufferDisplay(framebuffer)