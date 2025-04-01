import pygame


class GameLoop:
    def __init__(self, renderer, event_queue, clock):
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            current_time = self._clock.get_ticks()

            self._render()


            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()