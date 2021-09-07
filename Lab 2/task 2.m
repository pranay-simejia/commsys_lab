f=4;
hold on
for k=1:3
    f=f*10^3;
    w = 2 * pi * f;
    Roc = 280;
    ac = 0.0969;
    L0 = 587.3 * 10^-6;
    Linfi = 426 * 10^-6;
    b = 1.385;
    fm = 745900;
    Cf = 50 * 10^-9;
    Gf = 0;
    Rf = (Roc^4 + ac * f^2)^0.25;
    Lf = (L0 + Linfi * (f / fm)^b) / (1 + (f / fm)^b);
    y = ((Rf + w * Lf * 1i) * (Gf + w * Cf * 1i))^0.5;
    d = 0:500:5000;
    d(1) = 10;
    for j = 1:11
        x = d(j) / 1000;
        Hf(j) = 10log(abs(exp(-y * x)));
    end
     plot(d,Hf)
end
hold off