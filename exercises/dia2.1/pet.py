class Pet():
  def __init__(self, name, specie, age, human):
    self.name = name
    self.specie = specie
    self.age = age
    self.human = human

  def __str__(self):
    return f"""
    - name: {self.name}
    - specie: {self.specie}
    - age: {self.age}
    - human: {self.human}
    """
