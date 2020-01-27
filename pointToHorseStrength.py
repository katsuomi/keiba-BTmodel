const result = [1, 1, 1];

const calc = result => {
  const r1 = 10 / (result[0] + result[1]) + 10 / (result[0] + result[2]);
  const r2 = 10 / (result[1] + result[0]) + 10 / (result[1] + result[2]);
  const r3 = 10 / (result[2] + result[0]) + 10 / (result[2] + result[1]);

  const pipi1 = 7 / r1;
  const pipi2 = 9 / r2;
  const pipi3 = 14 / r3;

  let pi1 = (3 * pipi1) / (pipi1 + pipi2 + pipi3);
  let pi2 = (3 * pipi2) / (pipi1 + pipi2 + pipi3);
  let pi3 = (3 * pipi3) / (pipi1 + pipi2 + pipi3);
  pi1 = pi1 * 10000000;
  pi1 = Math.round(pi1);
  pi1 = pi1 / 10000000;
  pi2 = pi2 * 10000000;
  pi2 = Math.round(pi2);
  pi2 = pi2 / 10000000;
  pi3 = pi3 * 10000000;
  pi3 = Math.round(pi3);
  pi3 = pi3 / 10000000;
  result[0] = pi1;
  result[1] = pi2;
  result[2] = pi3;
  return result;
};

const result1 = calc(result)

const result2 = calc(result1)

const result3 = calc(result2)

const result4 = calc(result3)

const result5 = calc(result4)

const result6 = calc(result5)

const result7 = calc(result6)

const result8 = calc(result7)

const result9 = calc(result8)

const result10 = calc(result9)

const result11 = calc(result10)

const result12 = calc(result11)

const result13 = calc(result12)

const result14 = calc(result13)

const result15 = calc(result14)

const result16 = calc(result15)

const result17 = calc(result16)

const result18 = calc(result17)

const result19 = calc(result18)

const result20 = calc(result19)

const result21 = calc(result20)

const result22 = calc(result21)

const result23 = calc(result22)

const result24 = calc(result23)

const result25 = calc(result24)

const result26 = calc(result25)

const result27 = calc(result26)

const result28 = calc(result27)

const result29 = calc(result28)

const result30 = calc(result29)
