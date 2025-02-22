import torch

# Функция активации (ступенчатой функции округления)
def activation_function(x):
    return torch.round(x)
# Класс персептрона
class Perceptron:
    def __init__(self, num_inputs):
        # Инициализация весов случайными значениями
        self.weights = torch.rand(num_inputs, dtype=torch.float64)
        self.bias = torch.rand(1, dtype=torch.float64)  # Инициализация смещения случайным значением
    # Функция, вычисляющая выход персептрона
    def feed_forward(self, inputs):
        return activation_function(torch.sum(inputs * self.weights) + self.bias)
    # Функция обучения персептрона
    def train(self, inputs, target, learning_rate=0.1):
        output = self.feed_forward(inputs)
        error = target - output

        # Вывод входов, выходов и ошибки
        print(f"Входы: {inputs.tolist()} Выход: {int(output)} Ошибка: {int(error)}")

        # Обновление весов и смещения
        self.weights += error * inputs * learning_rate
        self.bias += error * learning_rate

# Основная функция
if __name__ == "__main__":
    # Создание персептрона с тремя входами
    perceptron = Perceptron(3)

    # Генерация последовательности из 25 целых десятичных чисел от 0 до 1
    sequence = [torch.randint(0, 2, (1,), dtype=torch.float64) for _ in range(25)]

    # Вывод сгенерированной последовательности
    print("Сгенерированная последовательность:")
    for i, item in enumerate(sequence):
        print(f"Число {i + 1}: {int(item.item())}")

    # Обучение персептрона для каждых трех чисел в последовательности
    total_error = 0
    for i in range(3, len(sequence)):
        input_data = torch.tensor([sequence[i - 3].item(), sequence[i - 2].item(), sequence[i - 1].item()])
        target = sequence[i].item()
        perceptron.train(input_data, target)
        total_error += abs(target - perceptron.feed_forward(input_data))

    average_train_error = total_error / (len(sequence) - 3)
    print(f"Средняя ошибка обучения: {average_train_error.item():.2f}")

    # Проверка обученного персептрона
    print("Проверка обученного персептрона:")
    total_error = 0
    for i in range(3, len(sequence)):
        input_data = torch.tensor([sequence[i - 3].item(), sequence[i - 2].item(), sequence[i - 1].item()])
        target = sequence[i].item()
        output = perceptron.feed_forward(input_data)
        error = abs(target - output)
        total_error += error
        print(f"Входы: {input_data.tolist()} | Ожидаемый вывод: {int(target)} | Предсказанный вывод: {int(output)} | Ошибка: {int(error)}")

    average_test_error = total_error / (len(sequence) - 3)
    print(f"Средняя ошибка обучения: {average_test_error.item():.2f}")