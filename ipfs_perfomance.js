const readline = require('readline');
const fs = require('fs');
const performance = require('perf_hooks').performance;

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

async function setupIPFS() {
    const IPFS = (await import('ipfs-http-client')).create;
    return IPFS({ host: 'localhost', port: 5001, protocol: 'http' });
}

function generatePayload(patientId) {
    return JSON.stringify({
        timestamp: new Date().toISOString(),
        patientId: patientId,
        block: {
            vitals: {
                bodyTemp: (36 + Math.random() * 4).toFixed(1),  // Temperature between 36.0 and 40.0
                pulseRate: Math.floor(60 + Math.random() * 40),  // Pulse rate between 60 and 100
                respirationRate: Math.floor(12 + Math.random() * 8),  // Respiration rate between 12 and 20
                bloodOxygen: Math.floor(90 + Math.random() * 10),  // Blood oxygen level between 90% and 100%
                glucoseLevel: Math.floor(70 + Math.random() * 130)  // Glucose level between 70 and 200 mg/dL
            }
        }
    });
}

async function measurePerformance(ipfs, iterations) {
    let addTimes = [];
    let retrieveTimes = [];

    for (let i = 0; i < iterations; i++) {
        const patientId = `Patient${i + 1}`;
        const jsonPayload = generatePayload(patientId);

        // Measure add performance
        const startTimeAdd = performance.now();
        const addedFile = await ipfs.add(jsonPayload);
        const endTimeAdd = performance.now();
        addTimes.push(endTimeAdd - startTimeAdd);

        // Measure retrieve performance
        const startTimeRetrieve = performance.now();
        for await (const chunk of ipfs.cat(addedFile.cid.toString())) {}
        const endTimeRetrieve = performance.now();
        retrieveTimes.push(endTimeRetrieve - startTimeRetrieve);
    }

    console.log(`Average Add Time: ${average(addTimes)} ms`);
    console.log(`Average Retrieve Time: ${average(retrieveTimes)} ms`);
}

function average(times) {
    return (times.reduce((acc, cur) => acc + cur, 0) / times.length).toFixed(2);
}

async function main() {
    const ipfs = await setupIPFS();
    await measurePerformance(ipfs, 500); // Measure performance for 10 iterations
}

main().catch(console.error);
