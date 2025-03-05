const themeButton = document.getElementById("theme-toggle");
const themeIcon = document.getElementById("theme-icon");
const body = document.body;

// Получаем пути к иконкам из data-атрибутов
const lightIcon = themeButton.dataset.light;
const darkIcon = themeButton.dataset.dark;

// Проверяем сохранённую тему
if (localStorage.getItem("theme") === "dark") {
    body.classList.add("dark-theme");
    themeIcon.src = darkIcon;
}

// Обработчик клика
themeButton.addEventListener("click", () => {
    body.classList.toggle("dark-theme");

    if (body.classList.contains("dark-theme")) {
        localStorage.setItem("theme", "dark");
        themeIcon.src = lightIcon; // Меняем иконку на "тёмную"
    } else {
        localStorage.setItem("theme", "light");
        themeIcon.src = darkIcon; // Меняем иконку на "светлую"
    }
});