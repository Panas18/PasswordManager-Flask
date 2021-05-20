let password_length = document.getElementById("password_len");
let password = document.getElementById("password");
let return_length = document.getElementById("length");
let generate = document.getElementById("generate");
let submit = document.getElementById("submit");
let view_password = document.getElementById("view");
return_length.innerHTML = password_length.value;
var generate_bool = false;

view.onclick = function () {
  if (password.type === "text") {
    password.type = "password";
  } else {
    password.type = "text";
  }
};

submit.onclick = function () {
  generate.value = false;
  password.value = null;
  password_length.disabled = true;
  view.value = false;
};

generate.onclick = function () {
  generate_bool = generate.checked;
  password_length.disabled = !generate_bool;
  if (generate_bool) {
    let current_password_length = password.value.length;
    if (!(current_password_length >= 1)) {
      password.value = generate_password(password_length.value);
    }
  }
};

password_length.oninput = function () {
  if (generate_bool) {
    password_length.disabled = false;
    return_length.innerHTML = this.value;
    let generated_password = generate_password(password_length.value);
    password.value = generated_password;
  }
};

function generate_password(length) {
  char =
    "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKlMNOPQRSTUVWXYZ][^_`abcdefghijklmnopqrstuvwxyz{|}~";

  let generated_password = "";

  for (let i = 0, n = char.length; i < length; i++) {
    generated_password += char.charAt(Math.floor(Math.random() * n));
  }
  return generated_password;
}
