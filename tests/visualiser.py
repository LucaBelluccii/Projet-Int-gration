import pygame as pg


IMG_PATH = "vector.jpg"

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
WINDOW_SURFACE = pg.HWSURFACE | pg.DOUBLEBUF | pg.RESIZABLE

PAN_BOX_WIDTH = 128
PAN_BOX_HEIGHT = 128
PAN_STEP = 5

pg.init()
window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_SURFACE)

base_image = pg.image.load(IMG_PATH).convert()


background = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
zoom_image = None

pan_box = pg.Rect(0, 0, PAN_BOX_WIDTH, PAN_BOX_HEIGHT)
last_box = pg.Rect(0, 0, 1, 1)


clock = pg.time.Clock()
done = False
while not done:

    for event in pg.event.get():
        if (event.type == pg.QUIT):
            done = True
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        pan_box.y -= PAN_STEP
    if keys[pg.K_DOWN]:
        pan_box.y += PAN_STEP
    if keys[pg.K_RIGHT]:
        pan_box.x += PAN_STEP
    if keys[pg.K_LEFT]:
        pan_box.x -= PAN_STEP
    if keys[pg.K_PLUS] or keys[pg.K_EQUALS]:
        pan_box.width = min(pan_box.width+PAN_STEP, WINDOW_WIDTH)
        pan_box.height = min(pan_box.height+PAN_STEP, WINDOW_HEIGHT)
    if keys[pg.K_MINUS]:
        pan_box.width = max(pan_box.width-PAN_STEP, PAN_STEP)
        pan_box.height = max(pan_box.height-PAN_STEP, PAN_STEP)
    PAN_BOX_WIDTH = min(PAN_BOX_WIDTH, base_image.get_width())
    PAN_BOX_HEIGHT = min(PAN_BOX_HEIGHT, base_image.get_height())
    pan_box.x = max(pan_box.x, 0)
    if pan_box.x + pan_box.width >= base_image.get_width():
        pan_box.x = base_image.get_width() - pan_box.width - 1
    pan_box.y = max(pan_box.y, 0)
    if pan_box.y + pan_box.height >= base_image.get_height():
        pan_box.y = base_image.get_height() - pan_box.height - 1
    
    if ( pan_box != last_box ):
        if ( pan_box.width != last_box.width or pan_box.height != last_box.height ):
            zoom_image = pg.Surface( ( pan_box.width, pan_box.height ) )  

        zoom_image.blit( base_image, ( 0, 0 ), pan_box )                  
        window_size = ( WINDOW_WIDTH, WINDOW_HEIGHT )
        pg.transform.scale( zoom_image, window_size, background )    
        last_box = pan_box.copy()
    window.blit( background, ( 0, 0 ) )
    pg.display.flip()
    clock.tick_busy_loop(60)
    
pg.quit()


window_size = ( WINDOW_WIDTH, WINDOW_HEIGHT )

zoom_image = pg.Surface( ( pan_box.width, pan_box.height ) )  
zoom_image.blit( base_image, ( 0, 0 ), pan_box )                   
pg.transform.scale( zoom_image, window_size, background )     

window.blit( background, ( 0, 0 ) )
pg.display.flip()