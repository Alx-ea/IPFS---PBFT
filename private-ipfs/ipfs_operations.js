const readline = require('readline');
const fs = require('fs');

async function setupIPFS() {
    const IPFS = (await import('ipfs-http-client')).create;
    return IPFS({ host: 'localhost', port: 5001, protocol: 'http' });
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

async function mainMenu(ipfs) {
    async function addFileToIPFS(filePath) {
        const file = fs.readFileSync(filePath);
        try {
            const addedFile = await ipfs.add(file);
            console.log(`Added file hash: ${addedFile.cid.toString()}`);
            return addedFile.cid.toString();
        } catch (error) {
            console.error('Error adding file to IPFS:', error);
        }
    }

    async function retrieveFileFromIPFS(ipfsHash) {
        try {
            const chunks = [];
            for await (const chunk of ipfs.cat(ipfsHash)) {
                chunks.push(chunk);
            }
            const data = Buffer.concat(chunks).toString();
            console.log('Retrieved file content:');
            console.log(data);
        } catch (error) {
            console.error('Error retrieving file from IPFS:', error);
        }
    }

    rl.question('Do you want to add a file or retrieve a file? (add/retrieve/exit): ', answer => {
        if (answer.toLowerCase() === 'add') {
            rl.question('Enter the path of the file to add: ', filePath => {
                addFileToIPFS(filePath).then(hash => {
                    console.log(`File added with hash: ${hash}`);
                    rl.close();
                }).catch(err => console.error(err));
            });
        } else if (answer.toLowerCase() === 'retrieve') {
            rl.question('Enter the IPFS hash of the file to retrieve: ', hash => {
                retrieveFileFromIPFS(hash).then(() => rl.close()).catch(err => console.error(err));
            });
        } else if (answer.toLowerCase() === 'exit') {
            rl.close();
        } else {
            console.log('Invalid input. Please type "add", "retrieve", or "exit".');
            mainMenu(ipfs);
        }
    });
}

(async () => {
    const ipfs = await setupIPFS();
    mainMenu(ipfs);
})();
