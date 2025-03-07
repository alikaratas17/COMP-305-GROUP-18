% n^3 = (100:50:500).^3, m = 200 -> should be linear in n^3
n_exp1 = (100:50:500);
n_cubed_exp1 = n_exp1.^3;
m_exp1 = 200;
times_exp1 = [
    sum([0.24,0.24,0.26,0.25])/4,
    sum([0.69,0.68,0.72,0.73])/4,
    sum([1.63,1.59,1.64,1.72])/4,
    sum([2.91,2.94,3.00,3.21])/4,
    sum([5.25,5.22,5.26,5.26])/4,
    sum([7.77,7.80,7.84,7.85])/4,
    sum([11.62,11.60,11.42,11.48])/4,
    sum([17.40,17.18,16.54,16.69])/4,
    sum([22.31,22.31,21.58,21.56])/4,
    ];
figure
plot(n_cubed_exp1,times_exp1)
xlabel("n^3 values")
ylabel("Time (s)")
title("Results of Time Analysis Experiment with m = 200, n from 100 to 500")

% m = (1000:1000:10000), n = 100 -> should be linear in m
m_exp2 = (1000:1000:10000);
n_exp2 = 100;
times_exp2 = [
    sum([1.14,1.14,1.17,1.24])/4,
    sum([2.36,2.34,2.47,2.49])/4,
    sum([3.40,3.41,3.58,3.58])/4,
    sum([5.00,5.02,4.50,4.52])/4,
    sum([6.30,6.29,6.19,6.22])/4,
    sum([7.16,7.18,7.92,7.90])/4,
    sum([9.16,9.17,9.07,9.04])/4,
    sum([10.21,10.17,10.63,10.59])/4,
    sum([12.34,12.51,12.46,12.44])/4,
    sum([14.63,14.73,14.08,14.05])/4,
    ];
figure
plot(m_exp2,times_exp2)
xlabel("m values")
ylabel("Time (s)")
title("Results of Time Analysis Experiment with n = 100, m from 1000 to 10000")


% n = 50, 100, 150, 200, 250; m =100
%n=500,m=100
case1_1 = [12.0,12.16,11.99];
case1_2 = [11.97,13.01,12.55];
case1_3 = [12.32,12.68,12.59];

%n=500,m=50
case2_1=[6.0,6.22,6.23];
case2_2=[6.33,6.48,6.55];
case2_3=[6.16,5.92,6.10];

% n = 100; m = 1000,
%n=100,m=500%
case3_1=[0.59,0.59,0.6];
case3_2=[0.62,0.62,0.62];
case3_3=[0.6,0.6,0.6];
%n=100, m=10000 %
case4 = [17.24,17.30,17.73];

avg = [sum(case1_1+case1_2+case1_3)/9,
    sum(case2_1+case2_2+case2_3)/9,
    sum(case3_1+case3_2+case3_3)/9,
    sum(case4)/3
    ];
figure
bar(avg)
title("Sample Runtimes")
xlabel("n,m Values")
ylabel("Runtimes (s)")
x = {'n = 500, m = 100',
    'n = 500, m = 50',
    'n = 100, m = 500',
    'n = 100, m = 10000'
    };
xticklabels(x)