import pygame

class GameLoop:
    def __init__(self, renderer, event_queue, clock):
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._textfield_active = False

    def start(self):
        while True:
            if self._handle_events() is False:
                break

            # current_time = self._clock.get_ticks()

            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if self._textfield_active:
                test = self._renderer.tf().handle_event(event)
                if test is True:
                    self._textfield_active = True
                elif test is False:
                    self._textfield_active = False
                else:
                    self._renderer.board.move(test)
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._textfield_active = self._renderer.tf().handle_event(event)

            if event.type == pygame.QUIT:
                return False
        return True

    def _render(self):
        self._renderer.render()
