from typing import Any, Optional


class queue:
    def __init__(self):
        self.__elements = []
      
    def arrive (self, value: Any) -> None:
        self.__elements.append(value)
      
    def atenttion(self) -> Optional[Any]:
        return(
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) -> int:
        return(len(self.__elements))
      
    def on_front(self) -> Optional[Any]:
        return(
            self.__elements.pop[0]
            if self.__elements
            else None
        )
      
    def move_to_end(self) -> Optional[Any]:
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value
          
    def show(self):
        for elemento in self.__elements:
            print(elemento)
