const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const fs = require('fs');
const { create } = require('ipfs-http-client');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());

// Setup IPFS connection
async function setupIPFS() {
    return create({ host: 'localhost', port: 5001, protocol: 'http' });
}

// Read file contents for IPFS
async function readFileContents(filePath) {
    return fs.readFileSync(filePath, { encoding: 'utf8' });
}

// Add file to IPFS and send data to PBFT
async function addFileToIPFSAndNotifyPBFT(ipfs, filePath) {
    try {
        const fileContents = await readFileContents(filePath);
        const addedFile = await ipfs.add({ content: fileContents });
        const hash = addedFile.cid.toString();
        console.log(`Added file hash: ${hash}`);

        // Construct PBFT payload
        const pbftData = {
            timestamp: new Date().toISOString(),
            patientId: "Patient1234",
            block: JSON.parse(fileContents)
        };

        // Send data to PBFT
        await axios.post('http://172.18.0.2:3002/createBlock', pbftData, {
            headers: {'Content-Type': 'application/json'}
        });
        return hash;
    } catch (error) {
        console.error('Error processing file:', error);
        throw error;
    }
}

// Express route to receive file path from IPFS notification
app.post('/notify-ipfs', async (req, res) => {
    const { filePath } = req.body;
    try {
        const ipfs = await setupIPFS();
        const hash = await addFileToIPFSAndNotifyPBFT(ipfs, filePath);
        res.send(`File processed and PBFT notified with IPFS hash: ${hash}`);
    } catch (error) {
        res.status(500).send('Failed to process file and notify PBFT');
    }
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
